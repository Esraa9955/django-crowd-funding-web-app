from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    total_target = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    
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


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reason = models.TextField()
          
