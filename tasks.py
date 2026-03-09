from invoke import task
import upload_drive

@task
def upload_zip(c, file="arquivo.zip"):
    """
    Envia um arquivo zipado para o Google Drive.
    """
    upload_drive.upload_to_drive(file_path=file)