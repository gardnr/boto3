import boto3

from gardnr import constants, drivers


class Boto3(drivers.Exporter):
    whitelist = [constants.Metrics.IMAGE]

    aws_access_key_id='ACCESS_KEY'
    aws_secret_access_key='SECRET_KEY'
    region_name = 'nyc3'
    endpoint_url='https://nyc3.digitaloceanspaces.com'
    bucket='my-bucket'

    def setup(self):
        session = boto3.session.Session()
        self.client = session.client(
            's3',
            region_name=self.region_name,
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key)

    def export(self, logs):
        for log in logs:
            self.client.upload_file(log.value,
                                    self.bucket,
                                    log.id)
