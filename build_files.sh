 echo "BUILD START"
 python3 -m pip install -r requirements.txt
 python3 manage.py collectstatic --noinput --clear
 echo "BUILD END"

 mkdir -p staticfiles_build
 mv generated_files/* staticfiles_build/