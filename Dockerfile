FROM python:2.7


# Install base packages and other software
#RUN apt-get update && apt-get install -y software-properties-common
#RUN add-apt-repository ppa:ubuntugis/ppa
#RUN apt-get install -y gdal-bin python-gdal
#RUN python -m ensurepip && \
#    rm -r /usr/lib/python*/ensurepip && \
#    pip install --upgrade distribute pip setuptools && \
#    rm -r /root/.cache

#FIX https://github.com/DefectDojo/django-DefectDojo/issues/407
RUN sed '/st_mysql_options options;/a unsigned int reconnect;' /usr/include/mysql/mysql.h -i.bkp

#FIX https://stackoverflow.com/questions/35780537/error-no-module-named-markerlib-when-installing-some-packages-on-virtualenv
RUN easy_install distribute
# RUN add-apt-repository ppa:ubuntugis/ppa && apt-get update && apt-get install -y gdal-bin python-gdal python3-gdal


WORKDIR /utopia-cms


EXPOSE 8000

ENTRYPOINT ["./local-entrypoint.sh"]

CMD ["python", "/utopia-cms/portal/manage.py", "runserver", "0.0.0.0:8000"]
