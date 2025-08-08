file_name = input("File name: ").strip().lower()

media_types = {
 ".gif": "image/gif",
 ".jpg": "image/jpeg",
 ".jpeg": "image/jpeg",
 ".png": "image/png",
 ".pdf": "application/pdf",
 ".txt": "text/plain",
 ".zip": "application/zip"
 }
for suffix, media_type in media_types.items():
  if file_name.endswith(suffix):
   print(media_type)
   break
  else:
   print("application/octet-stream")