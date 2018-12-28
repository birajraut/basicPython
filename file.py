try:
  file=open('testfile','w')
  file.write('ABCDEFG')
  try:
    file.write('\nhello')
  finally:
      print('hi')
      file.close()
except IOError:
 print('Konichiwa')