# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource


class PhoneNumberContext(InstanceContext):

    def __init__(self, version, phone_number):
        """
        Initialize the PhoneNumberContext
        
        :param Version version
        :param phone_number: The phone_number
        
        :returns: PhoneNumberContext
        :rtype: PhoneNumberContext
        """
        super(PhoneNumberContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'phone_number': phone_number,
        }
        self._uri = '/PhoneNumbers/{phone_number}'.format(**self._kwargs)

    def fetch(self, country_code=values.unset, type=values.unset):
        """
        Fetch a PhoneNumberInstance
        
        :param str country_code: The country_code
        :param str type: The type
        
        :returns: Fetched PhoneNumberInstance
        :rtype: PhoneNumberInstance
        """
        params = values.of({
            'CountryCode': country_code,
            'Type': type,
        })
        
        return self._version.fetch(
            PhoneNumberInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Lookups.V1.PhoneNumberContext {}>'.format(context)


class PhoneNumberInstance(InstanceResource):

    def __init__(self, version, payload, phone_number=None):
        """
        Initialize the PhoneNumberInstance
        
        :returns: PhoneNumberInstance
        :rtype: PhoneNumberInstance
        """
        super(PhoneNumberInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'country_code': payload['country_code'],
            'phone_number': payload['phone_number'],
            'national_format': payload['national_format'],
            'carrier': payload['carrier'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'phone_number': phone_number or self._properties['phone_number'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: PhoneNumberContext
        """
        if self._instance_context is None:
            self._instance_context = PhoneNumberContext(
                self._version,
                self._kwargs['phone_number'],
            )
        return self._instance_context

    @property
    def country_code(self):
        """
        :returns: The country_code
        :rtype: str
        """
        return self._properties['country_code']

    @property
    def phone_number(self):
        """
        :returns: The phone_number
        :rtype: str
        """
        return self._properties['phone_number']

    @property
    def national_format(self):
        """
        :returns: The national_format
        :rtype: str
        """
        return self._properties['national_format']

    @property
    def carrier(self):
        """
        :returns: The carrier
        :rtype: str
        """
        return self._properties['carrier']

    def fetch(self, country_code=values.unset, type=values.unset):
        """
        Fetch a PhoneNumberInstance
        
        :param str country_code: The country_code
        :param str type: The type
        
        :returns: Fetched PhoneNumberInstance
        :rtype: PhoneNumberInstance
        """
        return self._context.fetch(
            country_code=country_code,
            type=type,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Lookups.V1.PhoneNumberInstance {}>'.format(context)
