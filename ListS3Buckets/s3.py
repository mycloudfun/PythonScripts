#! /usr/bin/python3

import argparse, boto3, sys

def create_session(region, access_key, secret_key):
    try:
        if not access_key or not secret_key:
            return boto3.Session(
                region_name=region
            )
        else:
            return boto3.Session(
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region)
    except Exception as e:
        print("Something wrong while creating AWS session. ", e)
        sys.exit()

def list_s3(session, region):
          
	s3 = session.client('s3')

	try:
		for bucket in s3.list_buckets()['Buckets']:
			if s3.get_bucket_location(Bucket=bucket['Name'])['LocationConstraint'] == region:
				print(bucket['Name'])
	except Exception as e:
		print('Something went wrong: ', e)
		sys.exit()

def list_all_s3(session):
	try:
		s3 = session.client('s3').list_buckets()
	except Exception as e:
		print('Something went wrong: ', e)
		sys.exit()
	
	buckets = (s3['Buckets'])
	for buckets in buckets:
                print(buckets['Name'])

	
			
def main():
		all = 'all'
		regions = [
		'us-east-2',
		'us-east-1',
		'us-west-1',
		'us-west-2',
		'ap-south-1',
		'ap-northeast-3',
		'ap-northeast-2',
		'ap-southeast-1',
		'ap-southeast-2',
		'ap-northeast-1',
		'ca-central-1',
		'cn-north-1',
		'cn-northwest-1',
		'eu-central-1',
		'eu-west-1',
		'eu-west-2',
		'eu-west-3',
		'sa-east-1'
		]
		description = 'This script returns the list of S3 in given region or all regions'
		epilog = '''
-----------------------------
List of avilable regions:
-----------------------------''' + '\n' + all + '\n' + '\n'.join(regions)

		parser = argparse.ArgumentParser(description=description, epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)
		parser.add_argument("region", help="Region to scan, e.g. eu-west-1, all")
		parser.add_argument("-a", "--accesskey", help="AWS Access Key")
		parser.add_argument("-s", "--secretkey", help="AWS Secret Access Key")

		args = parser.parse_args()


		if args.region in regions:
			session = create_session(args.region, args.accesskey, args.secretkey)
			list_s3(session, args.region)
		elif args.region == all:
			session = create_session(regions[1], args.accesskey, args.secretkey)
			list_all_s3(session)
		else:
			print('''
----------------------------------
    Such region doesn't exist
----------------------------------
				''')
			parser.print_help()


if __name__ == "__main__":
        main()
