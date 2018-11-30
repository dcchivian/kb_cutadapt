FROM kbase/kbase:sdkbase2.latest
MAINTAINER KBase Developer [Michael Sneddon (mwsneddon@lbl.gov)]

# RUN apt-get update
RUN pip install --upgrade pip

# install cutadapt
RUN pip install cutadapt==1.14


COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod 777 /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
