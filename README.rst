=====================================================================
sbt-python-client: Wrapper for consuming `solutions by text REST API <https://www.solutionsbytext.com/api-support/api-documentation/>`_.
=====================================================================

sbt-python-client implements solutionsbytext REST APIs for python. 

============

* Python Python 3.5+

Install
============

The quick way::

    pip install scrapy


Typical usage often looks like this : 

1. Security Token

.. code-block:: python

        from solutions_by_text import create_security_token

        API_KEY = '<API_KEY_PROVIDED_BY_SBT>'

        # use 'ui' for production and 'test' for stagging APIs
        STAGE = 'test'
 
        security_token = create_security_token(API_KEY, STAGE)


1. Carrier

.. code-block:: python

        from solutions_by_text import carrier

        security_token = create_security_token(API_KEY, STAGE)

        carrier_object = carrier.CarrierLookUp(
            security_token=security_token,
            org_code='ORG_CODE',
            stage=STAGE,
            phone='<PHONE_NUMBER>')
        
        response = carrier_object.get()


2. Subscriber

.. code-block:: python

        from solutions_by_text import subscriber

        phones = '%s' % (["XXXXXXXXXX", "ZZZZZZZZZZ"])
        subscriber_object = subscriber.SubscriberStatus(
            security_token=security_token,
            org_code='ORG_CODE',
            stage=STAGE,
            phone=phones)

        response = subscriber_object.get()


2. Message

.. code-block:: python

        from solutions_by_text import message

        phone = "XXXXXXXXXX"
        my_message = "This is my text message"
        message_object = message.Message(
            security_token=security_token,
            org_code='ORG_CODE',
            stage=STAGE,
            phone=phone,
            message=my_message)

        response = message_object.send()