from django.db import models
from patient.models import Patient

class PatientData(models.Model):
    id = models.OneToOneField(Patient, primary_key=True, on_delete=models.CASCADE)
    medical_history = models.CharField
    active_seconds = models.FloatField
    net_activity_calories = models.FloatField
    distance_meters = models.FloatField
    steps = models.FloatField
    avg_hr_bpm = models.FloatField
    resting_hr_bpm = models.FloatField
    max_hr_bpm = models.FloatField
    min_hr_bpm = models.FloatField
    avg_stress_level = models.FloatField
    max_stress_level = models.FloatField

    sleep_avg_hr_bpm = models.FloatField
    sleep_max_hr_bpm = models.FloatField
    sleep_min_hr_bpm = models.FloatField
    sleep_avg_breaths_per_min = models.FloatField
    duration_REM_sleep_state_seconds = models.FloatField
    duration_asleep_state_seconds = models.FloatField
    duration_deep_sleep_state_seconds = models.FloatField
    duration_light_sleep_state_seconds = models.FloatField
    duration_in_bed_seconds = models.FloatField
    sleep_efficiency = models.FloatField

    class Meta:
        app_label = 'main'  

    def __str__(self):
        return f'Patient Data for {self.user.full_name}'