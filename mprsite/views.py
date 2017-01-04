from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import CurrentCourse, PastCourse
from .forms import MySignupForm
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from django.db.models import Q, Avg
from datetime import date
import random

@login_required(login_url='accounts/login/')
def index(request):
	#search db for courses via CRN, course number or course title
	search_results = None
	if request.GET.get('search'):
		search = request.GET.get('search')
		search_results = CurrentCourse.objects.filter(
			Q(crn__contains=search) | Q(course_number__icontains=search) | Q(course_title__icontains=search)
		)
	else:
		last = CurrentCourse.objects.count() - 1
		index1 = (random.randint(0, last) % 10) + 30
		index2 = random.randint(1, last - (index1 * 13) - 1)
		search_results = [CurrentCourse.objects.all()[index2 + (index1 * 1)],
							CurrentCourse.objects.all()[index2 + (index1 * 2)],
							CurrentCourse.objects.all()[index2 + (index1 * 3)],
							CurrentCourse.objects.all()[index2 + (index1 * 4)],
							CurrentCourse.objects.all()[index2 + (index1 * 5)],
							CurrentCourse.objects.all()[index2 + (index1 * 6)],
							CurrentCourse.objects.all()[index2 + (index1 * 7)],
							CurrentCourse.objects.all()[index2 + (index1 * 8)],
							CurrentCourse.objects.all()[index2 + (index1 * 9)],
							CurrentCourse.objects.all()[index2 + (index1 * 10)],
							CurrentCourse.objects.all()[index2 + (index1 * 11)],
							CurrentCourse.objects.all()[index2 + (index1 * 12)],
							CurrentCourse.objects.all()[index2 + (index1 * 13)]];


	profile = request.user.userprofile
	if profile.token_one != '':
		t_one = CurrentCourse.objects.get(crn=profile.token_one).course_number
	else:
		t_one = ''
	if profile.token_two != '':
		t_two = CurrentCourse.objects.get(crn=profile.token_two).course_number
	else:
		t_two = ''
	if profile.token_three != '':
		t_three = CurrentCourse.objects.get(crn=profile.token_three).course_number
	else:
		t_three = ''
	if profile.token_four != '':
		t_four = CurrentCourse.objects.get(crn=profile.token_four).course_number
	else:
		t_four = ''

	context = {'search_results': search_results, 't_one': t_one, 't_two': t_two, 't_three': t_three, 't_four': t_four}
	return render(request, 'mprsite/index.html', context);

@login_required(login_url='accounts/login/')
def course(request, course_num):
	max_val = 4
	up = request.user.userprofile
	course = get_object_or_404(CurrentCourse, course_number=course_num);
	gen_num = course.course_number[:-2];
	all_list = PastCourse.objects.filter(course_number__startswith=gen_num)
	last = all_list.count()
	#if last > 0:
	prof_list = all_list.filter(professor=course.professor).order_by('-year')
	recent_list = all_list.order_by('-year')

	'''
	if prof_list.count() >= max_val:
		prof_list = prof_list[max_val - 1]
	if recent_list.count() >= max_val:
		recent_list = recent_list[max_val - 1]
	'''

	avg_enroll = all_list.aggregate(Avg('filled_num_seats')).get('filled_num_seats__avg')
	avg_capac = all_list.aggregate(Avg('max_num_seats')).get('max_num_seats__avg')

	if avg_enroll is not None:
		avg_enroll = round(all_list.aggregate(Avg('filled_num_seats')).get('filled_num_seats__avg'), 1)
	if avg_capac is not None:
		avg_capac = round(all_list.aggregate(Avg('max_num_seats')).get('max_num_seats__avg'), 1)

	diff = up.grad_year - course.year;

	if diff % 1 == .5:
		feb = True
		diff -= .5
	else:
		feb = False

	if course.term.lower() == 'fall':
		diff -= 1

	if diff == -1:
		user = 'Super-Senior'
	elif diff == 0:
		user = 'Senior'
	elif diff == 1:
		user = 'Junior'
	elif diff == 2:
		user = 'Sophomore'
	else:
		user = 'Freshman'

	if up.token_one == course.crn:
		interest = True
	elif up.token_two == course.crn:
		interest = True
	elif up.token_three == course.crn:
		interest = True
	elif up.token_four == course.crn:
		interest = True
	else:
		interest = False

	if request.method == 'POST':

		if request.POST.get('Place Token'):
			changed = False
			if interest:
				print("User is already interested.")
			elif up.token_one == '':
				up.token_one = course.crn
				changed = True
			elif up.token_two == '':
				up.token_two = course.crn
				changed = True
			elif up.token_three == '':
				up.token_three = course.crn
				changed = True
			elif up.token_four == '':
				up.token_four = course.crn
				changed = True
			else:
				print('User has no free tokens.')

			if changed:
				up.save()
				interest = True
				course.num_tokens += 1

				if feb:
					if user == 'Senior':
						course.num_senior_febs += 1
					elif user == 'Junior':
						course.num_junior_febs += 1
					elif user == 'Sophomore':
						course.num_sophomore_febs += 1
					elif user == 'Freshman':
						course.num_freshman_febs += 1
					elif user == 'Super-Senior':
						course.num_super_senior_febs += 1
				else:
					if user == 'Senior':
						course.num_seniors += 1
					elif user == 'Junior':
						course.num_juniors += 1
					elif user == 'Sophomore':
						course.num_sophomores += 1
					elif user == 'Freshman':
						course.num_freshmen += 1

				course.save()

		elif request.POST.get('Remove Token'):
			changed = False
			if not interest:
				print('User is already not interested.')
			elif up.token_one == course.crn:
				up.token_one = ''
				changed = True
			elif up.token_two == course.crn:
				up.token_two = ''
				changed = True
			elif up.token_three == course.crn:
				up.token_three = ''
				changed = True
			elif up.token_four == course.crn:
				up.token_four = ''
				changed = True
			else:
				print('Something must have gone wrong...')

			if changed:
				up.save()
				interest = False
				course.num_tokens -= 1

				if feb:
					if user == 'Senior':
						course.num_senior_febs -= 1
					elif user == 'Junior':
						course.num_junior_febs -= 1
					elif user == 'Sophomore':
						course.num_sophomore_febs -= 1
					elif user == 'Freshman':
						course.num_freshman_febs -= 1
					elif user == 'Super-Senior':
						course.num_super_senior_febs -= 1
				else:
					if user == 'Senior':
						course.num_seniors -= 1
					elif user == 'Junior':
						course.num_juniors -= 1
					elif user == 'Sophomore':
						course.num_sophomores -= 1
					elif user == 'Freshman':
						course.num_freshmen -= 1

				course.save()

	context = {'course': course, 'prof_list': prof_list, 'recent_list': recent_list, 'gen': gen_num, 'interest': interest, 'avg_enroll': avg_enroll, 'avg_capac': avg_capac};

	return render(request, 'mprsite/course.html', context);


