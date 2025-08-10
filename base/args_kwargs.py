# why super(RegistrationForm, self).__init__(*args, **kwargs)
# not super(RegistrationForm, self).__init__(args, kwargs)

# super(RegistrationForm, self).__init__(*args, **kwargs)
# This is correct because it unpacks the arguments before passing them to the parent class’s  method.
#
#
# super(RegistrationForm, self).__init__(args, kwargs)
# This passes two arguments:
# • 	 as a single tuple
# • 	 as a single diction


# TypeError: __init__() takes from 1 to 2 positional arguments but 3 were given
# - *args unpacks the tuple into individual positional arguments.
# - **kwargs unpacks the dictionary into individual keyword arguments.
