from django.core.mail import send_mail as send_django_mail
from django.core.mail import EmailMultiAlternatives
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
def send_email_view(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')

        if not all([name, email, phone]):
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        subject = f"New Sponsor Form Submission from {name}"
        text_content = f"Name: {name}\nEmail: {email}\nPhone: {phone}"
        html_content = f"""
        <html>
            <body>
                <h1>Amara Hall of Fame Awards</h1>
                <h2>New Sponsor Form Submission</h2>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>
            </body>
        </html>
        """
        from_email = 'paulsandy321@gmail.com'  # Replace with your actual email
        recipient_list = ['paulsandy321@gmail.com']  # Replace with your recipient email(s)

        msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return Response({'message': 'Email sent successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
