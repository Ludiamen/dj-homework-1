from django.db import models


def image_path(instance, filename):
    return '/'.join(['sensors_images', f'sensor_id_{instance.sensor.id}', filename, ])


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )



# def image_path(instance, filename):
#     return '/'.join([
#         'sensors_images',
#         f'sensor_id_{instance.sensor.id}',
#         filename,
#     ])
#
#
# class Sensor(models.Model):
#     name = models.CharField(max_length=20)
#     description = models.CharField(max_length=40)
#
#
# class Measurement(models.Model):
#     sensor = models.ForeignKey(
#         Sensor,
#         on_delete=models.CASCADE,
#         related_name='measurements',
#     )
#     temp = models.FloatField()
#     image = models.ImageField(upload_to=image_path, null=True, blank=True)
#     created_at = models.DateField(auto_now_add=True)