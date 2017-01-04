from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grad_year = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    token_one = models.CharField(max_length=15, default='');
    token_two = models.CharField(max_length=15, default='');
    token_three = models.CharField(max_length=15, default='');
    token_four = models.CharField(max_length=15, default='');

def create_profile(sender, **kwargs):
	user = kwargs["instance"];
	if kwargs["created"]:
		user_profile = UserProfile(user=user);
		user_profile.save();
post_save.connect(create_profile, sender=User);

def assure_user_profile_exists(pk):
    """
    Creates a user profile if a User exists, but the
    profile does not exist.  Use this in views or other
    places where you don't have the user object but have the pk.
    """
    user = User.objects.get(pk=pk)
    #try:
        # fails if it doesn't exist
    userprofile = user.userprofile
    '''except UserProfile.DoesNotExist, e:
        userprofile = UserProfile(user=user)
        userprofile.save()'''
    return

#Want to be able to search via CRN, course number, course title?

class CurrentCourse(models.Model):
	crn = models.CharField(max_length = 5);
	course_title = models.CharField(max_length = 200);
	course_number = models.CharField(max_length = 15);
	year = models.PositiveSmallIntegerField(default = 0);
	term = models.CharField(max_length = 6);
	professor = models.CharField(max_length = 50);
	max_num_seats = models.PositiveSmallIntegerField(default = 0);
	filled_num_seats = models.PositiveSmallIntegerField(default = 0);
	waitlist_seats = models.PositiveSmallIntegerField(default = 0);
	filled_waitlist_seats = models.PositiveSmallIntegerField(default = 0);
	xlist_seats = models.PositiveSmallIntegerField(default = 0);
	filled_xlist_seats = models.PositiveSmallIntegerField(default = 0);
	start_time_one = models.CharField(max_length = 10);
	end_time_one = models.CharField(max_length = 10);
	start_time_two = models.CharField(max_length = 10);
	end_time_two = models.CharField(max_length = 10);
	days_one = models.CharField(max_length = 5);
	days_two = models.CharField(max_length = 5);
	location_one = models.CharField(max_length = 25);
	location_two = models.CharField(max_length = 25);
	cw = models.BooleanField(default = False);
	reserved_seats = models.PositiveSmallIntegerField(default = 0);
	num_tokens = models.PositiveSmallIntegerField(default = 0);
	num_seniors = models.PositiveSmallIntegerField(default = 0);
	num_juniors = models.PositiveSmallIntegerField(default = 0);
	num_sophomores = models.PositiveSmallIntegerField(default = 0);
	num_freshmen = models.PositiveSmallIntegerField(default = 0);
	num_super_senior_febs = models.PositiveSmallIntegerField(default = 0);
	num_senior_febs = models.PositiveSmallIntegerField(default = 0);
	num_junior_febs = models.PositiveSmallIntegerField(default = 0);
	num_sophomore_febs = models.PositiveSmallIntegerField(default = 0);
	num_freshman_febs = models.PositiveSmallIntegerField(default = 0);

class PastCourse(models.Model):
	crn = models.CharField(max_length = 5);
	course_title = models.CharField(max_length = 200);
	course_number = models.CharField(max_length = 15);
	year = models.PositiveSmallIntegerField(default = 0);
	term = models.CharField(max_length = 6);
	professor = models.CharField(max_length = 50);
	cw = models.BooleanField(default = False);
	max_num_seats = models.PositiveSmallIntegerField(default = 0);
	filled_num_seats = models.PositiveSmallIntegerField(default = 0);
	waitlist_seats = models.PositiveSmallIntegerField(default = 0);
	filled_waitlist_seats = models.PositiveSmallIntegerField(default = 0);
	xlist_seats = models.PositiveSmallIntegerField(default = 0);
	filled_xlist_seats = models.PositiveSmallIntegerField(default = 0);
	#reserved_seats = models.PositiveSmallIntegerField(default = 0);