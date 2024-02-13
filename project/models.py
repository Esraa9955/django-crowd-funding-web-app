from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    total_target = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    
    @classmethod
    def project_list(self):
        return self.objects.all()

    @classmethod
    def project_detailes(cls, proid):
        return cls.objects.get(id=proid)

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/images/', blank=True, null=True)   

    def project_image_detailes(cls, proid):
        return cls.objects.get(id=proid)

    def getimageurl(self):
        return f'/media/{self.image}'

