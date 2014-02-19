# Third party imports
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail


class CustomRegistrationView(RegistrationView):
    form_class = RegistrationFormUniqueEmail