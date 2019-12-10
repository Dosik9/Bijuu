# from django import forms
# from .models import Comment
#
# class CommentForm(forms.Form):
#     author_name = models.CharField(label ='Name of Author', max_length = 50)
#     comment_text = models.TextField("Comment text", max_length = 200)
#
#     def save(self):
#         new_comment = Comment.objects.create(
#             author_name= self.cleaned_data['author_name'],
#             comment_text = self.cleaned_data['comment_text']
#         )
#         return new_comment
