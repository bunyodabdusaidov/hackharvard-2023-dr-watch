from django.shortcuts import render
from .models import Patient

from terra.base_client import Terra
import uuid


def widget():
    patient = Patient.objects.create(id="554685b6-c42a-4ba9-9367-e367bdacb359")
    reference_id = str(patient.id)
    terra = Terra(
        api_key="EEFXq0ofN_SJ5fg7hzOb2r02HIw5wtUZ",
        dev_id="drwatch-testing-a1uqRDmD1q",
        secret="secret",
    )
    
    res = terra.generate_widget_session(
        providers=["GARMIN"],
        auth_success_redirect_url="https://example.com/success",
        auth_failure_redirect_url="https://example.com/failure",
        language="en",
        reference_id=reference_id,
    )
    
    return res.json['url']


def auth(request):
    session = widget()
    return render(request, 'index.html', {'terra':str(session)})


