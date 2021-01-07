import json
import smtplib 
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        return context

    def send_email(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)
        voting = get_object_or_404(Voting, pk=vid)

        if (voting.tally != 0):
            # definimos los correo de remitente y receptor
            ##se envia un mail a
            addr_to   = 'josgonman@alum.us.es'
            ##el mail sale desde el correo
            addr_from = 'semahsp16@gmail.com'

            # Define SMTP email server details
            smtp_server = 'smtp.gmail.com'
            smtp_user   = 'semahsp16@gmail.com'
            smtp_pass   = 'JM1995GM5991'
            
            # Construimos el mail
            msg = MIMEMultipart() 
            msg['To'] = addr_to
            msg['From'] = addr_from
            msg['Subject'] = 'Prueba'
            #cuerpo del mensaje en HTML y si fuera solo text puede colocar en el 2da parametro 'plain'
            msg.attach(MIMEText('< h1>Ya están los resultados de la votación< p>Aquí puede ver el resultado:\n http://localhost:8000/visualizer/'+ vid +'/','html'))

            # inicializamos el stmp para hacer el envio
            server = smtplib.SMTP(smtp_server, 587)
            server.starttls()
            #logeamos con los datos ya seteamos en la parte superior
            server.login(smtp_user,smtp_pass)
            #el envio
            server.sendmail(addr_from, addr_to, msg.as_string())
            #apagamos conexion stmp
            server.quit()
