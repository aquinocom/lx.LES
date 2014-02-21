from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class LxlesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import lx.LES
        xmlconfig.file(
            'configure.zcml',
            lx.LES,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'lx.LES:default')

LX_LES_FIXTURE = LxlesLayer()
LX_LES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LX_LES_FIXTURE,),
    name="LxlesLayer:Integration"
)
LX_LES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LX_LES_FIXTURE, z2.ZSERVER_FIXTURE),
    name="LxlesLayer:Functional"
)
