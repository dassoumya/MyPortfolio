import boto3
import StringIO as SIO
import zipfile
import mimetypes

s3 = boto3.resource('s3')
bucket = s3.Bucket('info.soumyaranjandas.com')
codebucket = s3.Bucket('codebuild.soumyaranjandas.com')

SIO = SIO.StringIO()
codebucket.download_fileobj('codebuild.zip/codebuild.zip',SIO)

with zipfile.ZipFile(SIO) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        bucket.Object(nm).Acl().put(ACL='public-read')
