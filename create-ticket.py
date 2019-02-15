def fetch_data():
  r = requests.get()
  requests.ConnectionError:
  r = requests.get(FALLBACK_MTG_JSON_URL)
  with closing(r), zipfile.ZipFile(io.BytesIO(r.content)) as archive:
  unzipped_files = archive.infolist()
    if len(unzipped_files) != 1:
      raise RuntimeError("Found an unexpected number of files in the MTGJSON archive.")
      data = archive.read(archive.infolist()[0])
      decoded_data = data.decode('utf-8')
      sets_data = json.loads(decoded_data)
      return(sets_data)
