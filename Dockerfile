FROM mitmproxy/mitmproxy

COPY ./ /code
WORKDIR /code
USER root

RUN pip install --disable-pip-version-check -r requirements.txt

USER mitmproxy
CMD mitmdump -s tunnel.py --ignore '^(?!pgorelease\.nianticlabs\.com)'
