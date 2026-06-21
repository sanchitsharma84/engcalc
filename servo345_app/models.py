from django.db import models

class SmallServoMotor(models.Model):
    make = models.CharField(max_length=20)
    motor_series = models.CharField(max_length=20)
    motor_model = models.CharField(max_length=50)
    shaft_height = models.CharField(max_length=20)
    rated_torque = models.FloatField()
    torque_at_0_rpm = models.FloatField()
    max_torque = models.FloatField()
    torque_at_max_rpm = models.FloatField()
    rated_rpm = models.IntegerField()
    max_rpm = models.IntegerField()
    rpm_at_max_torque = models.IntegerField()
    rated_power = models.FloatField()
    inertia_with_brake = models.FloatField()
    inertia_without_brake = models.FloatField()
    weight_with_brake = models.FloatField()
    weight_without_brake = models.FloatField()

    def __str__(self):
        return self.motor_series + '_' + str(self.rated_power) + 'kW_' + str(self.rated_rpm) + 'rpm_' + self.shaft_height

