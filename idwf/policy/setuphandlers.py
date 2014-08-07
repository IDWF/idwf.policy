from collective.grok import gs
from idwf.policy import MessageFactory as _

@gs.importstep(
    name=u'idwf.policy', 
    title=_('idwf.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('idwf.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
