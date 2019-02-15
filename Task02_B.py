def fetch_data():
  request = requests.get(www.abc.com/details)
  request1.ConnectionError:
  with closing(r), zipfile.ZipFile(io.BytesIO(request.content)) as archive:
  unzipped_files = archive.infolist()
    if len(unzipped_files) != 1:
      data = archive.read(archive.infolist()[0])
      decoded_data = data.decode('utf-8')
      post_data = json.loads(decoded_data)
      return(post_data)
