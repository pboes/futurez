"""Context Processor."""

from .forms import LoginForm

def check_login(request):
	login_form = LoginForm()
	if request.user.is_authenticated:
		return {'log_inf': True,
			'login_form': None
			}
	else:
		return {'log_inf': False,
			'login_form': login_form
			}
	
	return login_form

