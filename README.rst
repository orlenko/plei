.. image:: https://secure.travis-ci.org/orlenko/plei.png?branch=master
   :target: http://travis-ci.org/#!/orlenko/plei

Created by `Stephen McDonald <http://twitter.com/stephen_mcd>`_
Customized by `Vlad Orlenko <http://twitter.com/vorlenko>`_

========
Overview
========

Mezzanine is a powerful, consistent, and flexible content management
platform. Built using the `Django`_ framework, Mezzanine provides a
simple yet highly extensible architecture that encourages diving in
and hacking on the code. Mezzanine is `BSD licensed`_ and supported by
a diverse and active community.

In some ways, Mezzanine resembles tools such as `Wordpress`_ that
provide an intuitive interface for managing pages, blog posts, form
data, store products, and other types of content. But Mezzanine is
also different. Unlike many other platforms that make extensive use of
modules or reusable applications, Mezzanine provides most of its
functionality by default. This approach yields a more integrated and
efficient platform.

Visit the `Mezzanine project page`_ to see some of the `great sites
people have built using Mezzanine`_.

Features
========

In addition to the usual features provided by Django such as MVC
architecture, ORM, templating, caching and an automatic admin
interface, Mezzanine provides the following:

  * Hierarchical page navigation
  * Save as draft and preview on site
  * Scheduled publishing
  * Drag-and-drop page ordering
  * WYSIWYG editing
  * `In-line page editing`_
  * Drag-and-drop HTML5 forms builder with CSV export
  * SEO friendly URLs and meta data
  * Shopping cart module (`Cartridge`_)
  * Configurable `dashboard`_ widgets
  * Blog engine
  * Tagging
  * User accounts and profiles with email verification
  * Translated to over 20 languages
  * Sharing via Facebook or Twitter
  * `Custom templates`_ per page or blog post
  * `Twitter Bootstrap`_ integration
  * API for `custom content types`_
  * `Search engine and API`_
  * Seamless integration with third-party Django apps
  * Multi-device detection and template handling
  * One step migration from other blogging engines
  * Automated production provisioning and deployments
  * `Disqus`_ integration, or built-in threaded comments
  * `Gravatar`_ integration
  * `Google Analytics`_ integration
  * `Twitter`_ feed integration
  * `bit.ly`_ integration
  * `Akismet`_ spam filtering
  * Built-in `test suite`_
  * `JVM`_ compatible (via `Jython`_)

The Mezzanine admin dashboard:

.. image:: http://github.com/orlenko/plei/raw/master/docs/img/dashboard.png

Dependencies
============

Mezzanine makes use of as few libraries as possible (apart from a
standard Django environment), with the following dependencies:

  * `Python`_ 2.6 / 2.7
  * `Django`_ 1.4 / 1.5
  * `Python Imaging Library`_ - for image resizing
  * `grappelli-safe`_ - admin skin (`Grappelli`_ fork)
  * `filebrowser-safe`_ - for managing file uploads (`FileBrowser`_ fork)
  * `bleach`_ - for sanitizing markup in content
  * `pytz`_ - for timezone support
  * `South`_ - for database migrations (optional)
  * `django-compressor`_ - for merging JS/CSS assets (optional)
  * `pyflakes`_ and `pep8`_ - for running the test suite (optional)

Browser Support
===============

Mezzanine's admin interface works with all modern browsers.
Internet Explorer 7 and earlier are generally unsupported.

Installation
============

The easiest method is to install directly from pypi using `pip`_ by
running the command below, which will also install the required
dependencies mentioned above::

    $ pip install plei

If you prefer, you can download Mezzanine and install it directly from
source::

    $ python setup.py install

Once installed, the command ``plei-project`` can be used to
create a new Mezzanine project in similar fashion to
``django-admin.py``::

    $ plei-project project_name
    $ cd project_name
    $ python manage.py createdb --noinput
    $ python manage.py runserver

.. note::

    The ``createdb`` command is a shortcut for using Django's ``syncdb``
    command and setting the initial migration state for `South`_. You
    can alternatively use ``syncdb`` and ``migrate`` if preferred.
    South is automatically added to INSTALLED_APPS if the
    ``USE_SOUTH`` setting is set to ``True``.

    ``createdb`` will also install some demo content, such as a contact
    form and image gallery. If you'd like to omit this step, use the
    ``--nodata`` option with ``createdb``.

You should then be able to browse to http://127.0.0.1:8000/admin/ and
log in using the default account (``username: admin, password:
default``). If you'd like to specify a different username and password
during set up, simply exclude the ``--noinput`` option included above
when running ``createdb``.

For information on how to add Mezzanine to an existing Django project,
see the FAQ section of the documentation.

Contributing
============

Mezzanine is an open source project managed using both the Git and
Mercurial version control systems. These repositories are hosted on
both `GitHub`_ and `Bitbucket`_ respectively, so contributing is as
easy as forking the project on either of these sites and committing
back your enhancements.

Please note the following guidelines for contributing:

  * Contributed code must be written in the existing style. This is
    as simple as following the `Django coding style`_ and (most
    importantly) `PEP 8`_.
  * Contributions must be available on a separately named branch
    based on the latest version of the main branch.
  * Run the tests before committing your changes. If your changes
    cause the tests to break, they won't be accepted.
  * If you are adding new functionality, you must include basic tests
    and documentation.

If you want to do development with plei, here's a quick way to set
up a development environment and run the unit tests, using
`virtualenvwrapper`_ to set up a virtualenv::

    $ mkvirtualenv plei
    $ workon plei
    $ pip install Django pep8 pyflakes
    $ git clone https://github.com/orlenko/plei/
    $ cd plei
    $ python setup.py develop
    $ cp plei/project_template/local_settings.py.template plei/project_template/local_settings.py
    $ ./plei/project_template/manage.py test


Language Translations
=====================

Mezzanine makes full use of translation strings, which allow Mezzanine
to be translated into multiple languages using `Django's
internationalization`_ methodology. Translations are managed on the
`Transiflex`_ website but can also be submitted via `GitHub`_ or
`Bitbucket`_. Consult the documentation for `Django's
internationalization`_ methodology for more information on creating
translations and using them.

Third-party Modules
===================

The following modules have been developed outside of Mezzanine. If you
have developed a module to integrate with Mezzanine and would like to
list it here, send an email to the `plei-users`_ mailing list.
You can also add modules to the `Mezzanine Grid on djangopackages.com`_.

  * `plei-html5boilerplate`_ - Integrates the
    `html5boilerplate project`_  into Mezzanine.
  * `plei-mdown`_ - Adds `Markdown`_ support to Mezzanine's rich
    text editor.
  * `plei-openshift`_ - Setup for running Mezzanine on
    `Redhat's OpenShift`_ cloud platform.
  * `plei-stackato`_ - Setup for running Mezzanine on
    `ActiveState's Stackato`_ cloud platform.
  * `plei-blocks`_ - A Mezzanine flavored fork of
    django-flatblocks.
  * `plei-widgets`_ - Widget system for Mezzanine.
  * `plei-themes`_ - A collection of Django/Mezzanine templates.
  * `plei-twittertopic`_ - Manage multiple Twitter topic feeds
    from the Mezzanine admin interface.
  * `plei-captcha`_ - Adds CAPTCHA field types to Mezzanine's
    forms builder app.
  * `plei-bookmarks`_ - A multi-user bookmark app for Mezzanine.
  * `plei-events`_ - Events plugin for Mezzanine, with geocoding
    via Google Maps, iCalendar files, webcal URLs and directions via
    Google Calendar/Maps.
  * `plei-polls`_ - Polls application for Mezzanine.
  * `plei-pagedown`_ - Adds the `Pagedown`_ WYSIWYG editor to
    Mezzanine.
  * `plei-careers`_ - Job posting application for Mezzanine.
  * `plei-recipes`_ - Recipes plugin with built-in REST API.
  * `plei-slides`_ - Responsive banner slides app for Mezzanine.
  * `mezzyblocks`_ - Another app for adding blocks/modules to Mezzanine.
  * `plei-flexipage`_ - Allows designers to manage content areas
    in templates.
  * `plei-instagram`_ - A simple Instagram app for Mezzanine.
  * `plei-wiki`_ - Wiki app for Mezzanine.
  * `plei-calendar`_ - Calendar pages in Mezzanine
  * `plei-facebook`_ - Simple Facebook integration for Mezzanine.
  * `plei-instagram-gallery`_ - Create Mezzanine galleries using
    Instagram images.
  * `plei-cli`_ - Command-line interface for Mezzanine.
  * `plei-categorylink`_ - Integrates Mezzanine's Link pages with
    its blog categories.
  * `plei-podcast`_ - A simple podcast streamer and manager for
    Mezzanine.
  * `plei-linkcollection`_ - Collect links. Feature them. Share
    them over RSS.
  * `cash-generator`_ - Generate `GnuCash`_ invoices with Mezzanine.
  * `plei-foundation`_ - `Zurb Foundation`_ theme for Mezzanine.
  * `plei-file-collections`_ - Simple file collection page type for Mezzanine.

Donating
========

If you would like to make a donation to continue development of
Mezzanine, you can do so via the `Mezzanine Project`_ website.

Support
=======

To report a security issue, please send an email privately to
`security@jupo.org`_. This gives us a chance to fix the issue and
create an official release prior to the issue being made
public.

For general questions or comments, please join the `plei-users`_
mailing list. To report a bug or other type of issue, please use the
`GitHub issue tracker`_. And feel free to drop by the `#plei
IRC channel`_ on `Freenode`_, for a chat.

Communications in all Mezzanine spaces are expected to conform
to the `Django Code of Conduct`_.

Sites Using Mezzanine
=====================

  * `Citrus Agency <http://citrus.com.au/>`_
  * `Mezzanine Project <http://plei.jupo.org>`_
  * `Nick Hagianis <http://hagianis.com>`_
  * `Thomas Johnson <http://tomfmason.net>`_
  * `Central Mosque Wembley <http://wembley-mosque.co.uk>`_
  * `Ovarian Cancer Research Foundation <http://ocrf.com.au/>`_
  * `The Source Procurement <http://thesource.com.au/>`_
  * `Imageinary <http://imageinary.com>`_
  * `Brad Montgomery <http://blog.bradmontgomery.net>`_
  * `Jashua Cloutier <http://www.senexcanis.com>`_
  * `Alpha & Omega Contractors <http://alphaomegacontractors.com>`_
  * `Equity Advance <http://equityadvance.com.au/>`_
  * `Head3 Interactive <http://head3.com>`_
  * `PyLadies <http://www.pyladies.com>`_
  * `Ripe Maternity <http://www.ripematernity.com/>`_
  * `Cotton On <http://shop.cottonon.com/>`_
  * `List G Barristers <http://www.listgbarristers.com.au>`_
  * `Tri-Cities Flower Farm <http://www.tricitiesflowerfarm.com>`_
  * `daon.ru <http://daon.ru/>`_
  * `autoindeks.ru <http://autoindeks.ru/>`_
  * `immiau.ru <http://immiau.ru/>`_
  * `ARA Consultants <http://www.araconsultants.com.au/>`_
  * `Boîte à Z'images <http://boiteazimages.com/>`_
  * `The Melbourne Cup <http://www.melbournecup.com/>`_
  * `Diablo News <http://www.diablo-news.com>`_
  * `Goldman Travel <http://www.goldmantravel.com.au/>`_
  * `IJC Digital <http://ijcdigital.com/>`_
  * `Coopers <http://store.coopers.com.au/>`_
  * `Joe Julian <http://joejulian.name>`_
  * `Sheer Ethic <http://sheerethic.com/>`_
  * `Salt Lake Magazine <http://saltlakemagazine.com/>`_
  * `Boca Raton Magazine <http://bocamag.com/>`_
  * `Photog.me <http://www.photog.me>`_
  * `Elephant Juice Soup <http://www.elephantjuicesoup.com>`_
  * `National Positions <http://www.nationalpositions.co.uk/>`_
  * `Like Humans Do <http://www.likehumansdo.com>`_
  * `Connecting Countries <http://connectingcountries.net>`_
  * `tindie.com <http://tindie.com>`_
  * `Environmental World Products <http://ewp-sa.com/>`_
  * `Ross A. Laird <http://rosslaird.com>`_
  * `Etienne B. Roesch <http://etienneroes.ch>`_
  * `Recruiterbox <http://recruiterbox.com/>`_
  * `Mod Productions <http://modprods.com/>`_
  * `Appsembler <http://appsembler.com/>`_
  * `Pink Twig <http://www.pinktwig.ca>`_
  * `Parfume Planet <http://parfumeplanet.com>`_
  * `Trading 4 Us <http://www.trading4.us>`_
  * `Chris Fleisch <http://chrisfleisch.com>`_
  * `Theneum <http://theneum.com/>`_
  * `My Story Chest <http://www.mystorychest.com>`_
  * `Philip Sahli <http://www.fatrix.ch>`_
  * `Raymond Chandler <http://www.codearchaeologist.org>`_
  * `Nashsb <http://nashpp.com>`_
  * `AciBASE <http://acinetobacter.bham.ac.uk>`_
  * `Enrico Tröger <http://www.uvena.de>`_
  * `Matthe Wahn <http://www.matthewahn.com>`_
  * `Bit of Pixels <http://bitofpixels.com>`_
  * `European Crystallographic Meeting <http://ecm29.ecanews.org>`_
  * `Dreamperium <http://dreamperium.com>`_
  * `UT Dallas <http://utdallasiia.com>`_
  * `Go Yama <http://goyamamusic.com>`_
  * `Yeti LLC <http://www.yetihq.com/>`_
  * `Li Xiong <http://idhoc.com>`_
  * `Pageworthy <http://pageworthy.com>`_
  * `Prince Jets <http://princejets.com>`_
  * `30 sites in 30 days <http://1inday.com>`_
  * `St Barnabas' Theological College <http://www.sbtc.org.au>`_
  * `Helios 3D <http://helios3d.nl/>`_
  * `Life is Good <http://lifeisgoodforall.co.uk/>`_
  * `Brooklyn Navy Yard <http://bldg92.org/>`_
  * `Pie Monster <http://piemonster.me>`_
  * `Cotton On Asia <http://asia.cottonon.com/>`_
  * `Ivan Diao <http://www.adieu.me>`_
  * `Super Top Secret <http://www.wearetopsecret.com/>`_
  * `Jaybird Sport <http://www.jaybirdgear.com/>`_
  * `Manai Glitter <https://manai.co.uk>`_
  * `Sri Emas International School <http://www.sriemas.edu.my>`_
  * `Boom Perun <http://perunspace.ru>`_
  * `Tactical Bags <http://tacticalbags.ru>`_
  * `apps.de <http://apps.de>`_
  * `Sunfluence <http://sunfluence.com>`_
  * `ggzpreventie.nl <http://ggzpreventie.nl>`_
  * `dakuaiba.com <http://www.dakuaiba.com>`_
  * `Wdiaz <http://www.wdiaz.org>`_
  * `Hunted Hive <http://huntedhive.com/>`_
  * `mjollnir.org <http://mjollnir.org>`_
  * `The Beancat Network <http://www.beancatnet.org>`_
  * `Raquel Marón <http://raquelmaron.com/>`_
  * `EatLove <http://eatlove.com.au/>`_
  * `Hospitality Quotient <http://hospitalityq.com/>`_
  * `The Andrew Story <http://theandrewstory.com/>`_
  * `Charles Koll Jewelry <http://charleskoll.com/>`_
  * `Mission Healthcare <http://homewithmission.com/>`_
  * `Creuna (com/dk/fi/no/se) <http://www.creuna.com/>`_
  * `Coronado School of the Arts <http://www.cosasandiego.com/>`_
  * `SiteComb <http://www.sitecomb.com>`_
  * `Dashing Collective <http://dashing.tv/>`_
  * `Puraforce Remedies <http://puraforceremedies.com/>`_
  * `Google's VetNet <http://www.vetnethq.com/>`_
  * `1800RESPECT <http://www.1800respect.org.au/>`_
  * `Evenhouse Consulting <http://evenhouseconsulting.com/>`_
  * `Humboldt Community Christian School <http://humboldtccs.org>`_
  * `Atlanta's Living Legacy <http://gradyhistory.com>`_
  * `Shipgistix <http://shipgistix.com>`_
  * `Yuberactive <http://www.yuberactive.asia>`_
  * `Medical Myth Busters <http://pogromcymitowmedycznych.pl>`_
  * `4player Network <http://4playernetwork.com/>`_
  * `Top500 Supercomputers <http://top500.org>`_
  * `Die Betroffenen <http://www.zeichnemit.de>`_
  * `uvena.de <http://uvena.de>`_
  * `ezless.com <http://ezless.com>`_
  * `Dominican Python <http://python.do>`_
  * `Stackful.io <http://stackful.io/>`_
  * `Adrenaline <http://www.adrln.com/>`_
  * `ACE EdVenture Programme <http://aceedventure.com/>`_
  * `Butchershop Creative <http://www.butchershopcreative.com/>`_
  * `Sam Kingston <http://www.sjkingston.com>`_
  * `Ludwig von Mises Institute <http://mises.fi>`_
  * `Incendio <http://incendio.no/>`_
  * `Alexander Lillevik <http://lillevikdesign.no/>`_
  * `Walk In Tromsø <http://www.turitromso.no>`_
  * `Mandrivia Linux <http://www.mandriva.com/>`_
  * `Crown Preschool <http://crownpreschool.com>`_
  * `Coronado Pathways Charter School <http://coronadopathways.com>`_
  * `Raindrop Marketing <http://www.raindropads.com>`_
  * `Web4py <http://www.web4py.com>`_
  * `The Peculiar Store <http://thepeculiarstore.com>`_
  * `GrinDin <http://www.grindin.ru>`_
  * `4Gume <http://www.4gume.com>`_
  * `Skydivo <http://skydivo.com>`_
  * `Noshly <http://noshly.com>`_
  * `Kabu Creative <http://kabucreative.com.au/>`_
  * `KisanHub <http://www.kisanhub.com/>`_
  * `Your Song Your Story <http://yoursongyourstory.org/>`_
  * `Kegbot <http://kegbot.org>`_
  * `Fiz <http://fiz.com/>`_
  * `Willborn <http://willbornco.com>`_
  * `Copilot Co <http://copilotco.com>`_
  * `Amblitec <http://www.amblitec.com>`_
  * `Gold's Gym Utah <http://www.bestgymever.com/>`_
  * `Appsin - Blog to Native app <http://apps.in/>`_
  * `Take Me East <http://takemeeast.net>`_
  * `Code Raising <http://www.coderaising.org>`_
  * `ZigZag Bags <http://www.zigzagbags.com.au>`_


Quotes
======

  * "I'm enjoying working with Mezzanine, it's good work"
    - `Van Lindberg`_, `Python Software Foundation`_ chairman
  * "Mezzanine looks like it may be Django's killer app"
    - `Antonio Rodriguez`_, ex CTO of `Hewlett Packard`_, founder
    of `Tabblo`_
  * "Mezzanine looks pretty interesting, tempting to get me off
    Wordpress" - `Jesse Noller`_, Python core contributor,
    `Python Software Foundation`_ board member
  * "I think I'm your newest fan. Love these frameworks"
    - `Emile Petrone`_, integrations engineer at `Urban Airship`_
  * "Mezzanine is amazing" - `Audrey Roy`_, founder of `PyLadies`_
    and `Django Packages`_
  * "Mezzanine convinced me to switch from the Ruby world over
    to Python" - `Michael Delaney`_, developer
  * "Like Linux and Python, Mezzanine just feels right" - `Phil Hughes`_,
    Linux For Dummies author, `The Linux Journal`_ columnist
  * "Impressed with Mezzanine so far" - `Brad Montgomery`_, founder
    of `Work For Pie`_
  * "From the moment I installed Mezzanine, I have been delighted, both
    with the initial experience and the community involved in its
    development" - `John Campbell`_, founder of `Head3 Interactive`_
  * "You need to check out the open source project Mezzanine. In one
    word: Elegant" - `Nick Hagianis`_, developer

.. GENERAL LINKS

.. _`Django`: http://djangoproject.com/
.. _`Django Code of Conduct`: https://www.djangoproject.com/conduct/
.. _`BSD licensed`: http://www.linfo.org/bsdlicense.html
.. _`Wordpress`: http://wordpress.org/
.. _`great sites people have built using Mezzanine`: http://plei.jupo.org/sites/
.. _`Pinax`: http://pinaxproject.com/
.. _`Mingus`: http://github.com/montylounge/django-mingus
.. _`Mezzanine project page`: http://plei.jupo.org
.. _`Python`: http://python.org/
.. _`pip`: http://www.pip-installer.org/
.. _`bleach`: http://pypi.python.org/pypi/bleach
.. _`pytz`: http://pypi.python.org/pypi/pytz/
.. _`django-compressor`: https://pypi.python.org/pypi/django_compressor
.. _`Python Imaging Library`: http://www.pythonware.com/products/pil/
.. _`grappelli-safe`: http://github.com/orlenko/grappelli-safe
.. _`filebrowser-safe`: http://github.com/orlenko/filebrowser-safe/
.. _`Grappelli`: http://code.google.com/p/django-grappelli/
.. _`FileBrowser`: http://code.google.com/p/django-filebrowser/
.. _`South`: http://south.aeracode.org/
.. _`pyflakes`: http://pypi.python.org/pypi/pyflakes
.. _`pep8`: http://pypi.python.org/pypi/pep8
.. _`In-line page editing`: http://plei.jupo.org/docs/inline-editing.html
.. _`custom content types`: http://plei.jupo.org/docs/content-architecture.html#creating-custom-content-types
.. _`Search engine and API`: http://plei.jupo.org/docs/search-engine.html
.. _`dashboard`: http://plei.jupo.org/docs/admin-customization.html#dashboard
.. _`Cartridge`: http://cartridge.jupo.org/
.. _`Themes`: http://plei.jupo.org/docs/themes.html
.. _`Custom templates`: http://plei.jupo.org/docs/content-architecture.html#page-templates
.. _`test suite`: http://plei.jupo.org/docs/packages.html#module-plei.core.tests
.. _`JVM`: http://en.wikipedia.org/wiki/Java_virtual_machine
.. _`Jython`: http://www.jython.org/
.. _`Twitter Bootstrap`: http://twitter.github.com/bootstrap/
.. _`Disqus`: http://disqus.com/
.. _`Gravatar`: http://gravatar.com/
.. _`Google Analytics`: http://www.google.com/analytics/
.. _`Twitter`: http://twitter.com/
.. _`bit.ly`: http://bit.ly/
.. _`Akismet`: http://akismet.com/
.. _`project_template`: https://github.com/orlenko/plei/tree/master/plei/project_template
.. _`GitHub`: http://github.com/orlenko/plei/
.. _`Bitbucket`: http://bitbucket.org/orlenko/plei/
.. _`plei-users`: http://groups.google.com/group/plei-users/topics
.. _`security@jupo.org`: mailto:security@jupo.org?subject=Mezzanine+Security+Issue
.. _`GitHub issue tracker`: http://github.com/orlenko/plei/issues
.. _`#plei IRC channel`: irc://freenode.net/plei
.. _`Freenode`: http://freenode.net
.. _`Django coding style`: http://docs.djangoproject.com/en/dev/internals/contributing/#coding-style
.. _`PEP 8`: http://www.python.org/dev/peps/pep-0008/
.. _`Transiflex`: https://www.transifex.net/projects/p/plei/
.. _`Mezzanine Grid on djangopackages.com`: http://www.djangopackages.com/grids/g/plei/
.. _`Django's internationalization`: https://docs.djangoproject.com/en/dev/topics/i18n/translation/
.. _`Python Software Foundation`: http://www.python.org/psf/
.. _`Urban Airship`: http://urbanairship.com/
.. _`Django Packages`: http://djangopackages.com/
.. _`Hewlett Packard`: http://www.hp.com/
.. _`Tabblo`: http://www.tabblo.com/
.. _`The Linux Journal`: http://www.linuxjournal.com
.. _`Work For Pie`: http://workforpie.com/
.. _`virtualenvwrapper`: http://www.doughellmann.com/projects/virtualenvwrapper


.. THIRD PARTY LIBS

.. _`plei-html5boilerplate`: https://github.com/tvon/plei-html5boilerplate
.. _`html5boilerplate project`: http://html5boilerplate.com/
.. _`plei-mdown`: https://bitbucket.org/onelson/plei-mdown
.. _`Markdown`: http://en.wikipedia.org/wiki/Markdown
.. _`plei-openshift`: https://github.com/overshard/plei-openshift
.. _`Redhat's OpenShift`: https://openshift.redhat.com/
.. _`plei-stackato`: https://github.com/Stackato-Apps/plei
.. _`ActiveState's Stackato`: http://www.activestate.com/stackato
.. _`plei-blocks`: https://github.com/renyi/plei-blocks
.. _`plei-widgets`: https://github.com/osiloke/plei_widgets
.. _`plei-themes`: https://github.com/renyi/plei-themes
.. _`plei-twittertopic`: https://github.com/lockhart/plei-twittertopic
.. _`plei-captcha`: https://github.com/mjtorn/plei-captcha
.. _`plei-bookmarks`: https://github.com/adieu/plei-bookmarks
.. _`plei-events`: https://github.com/stbarnabas/plei-events
.. _`plei-polls`: https://github.com/sebasmagri/plei_polls
.. _`plei-pagedown`: https://bitbucket.org/akhayyat/plei-pagedown
.. _`PageDown`: https://code.google.com/p/pagedown/
.. _`plei-careers`: https://github.com/mogga/plei-careers
.. _`plei-recipes`: https://github.com/tjetzinger/plei-recipes
.. _`plei-slides`: https://github.com/overshard/plei-slides
.. _`mezzyblocks`: https://github.com/jardaroh/mezzyblocks
.. _`plei-flexipage`: https://github.com/mrmagooey/plei-flexipage
.. _`plei-wiki`: https://github.com/dfalk/plei-wiki
.. _`plei-instagram`: https://github.com/shurik/Mezzanine_Instagram
.. _`plei-calendar`: https://github.com/shurik/plei.calendar
.. _`plei-facebook`: https://github.com/shurik/Mezzanine_Facebook
.. _`plei-instagram-gallery`: https://github.com/georgeyk/plei-instagram-gallery
.. _`plei-cli`: https://github.com/adieu/plei-cli
.. _`plei-categorylink`: https://github.com/mjtorn/plei-categorylink
.. _`plei-podcast`: https://github.com/carpie/plei-podcast
.. _`plei-linkcollection`: https://github.com/mjtorn/plei-linkcollection
.. _`cash-generator`: https://github.com/ambientsound/cash-generator
.. _`GnuCash`: http://www.gnucash.org/
.. _`plei-foundation`: https://github.com/zgohr/plei-foundation
.. _`Zurb Foundation`: http://foundation.zurb.com/
.. _`plei-file-collections`: https://github.com/thibault/plei-file-collections


.. PEOPLE WITH QUOTES

.. _`Van Lindberg`: http://www.lindbergd.info/
.. _`Antonio Rodriguez`: http://an.ton.io/
.. _`Jesse Noller`: http://jessenoller.com/
.. _`Emile Petrone`: https://twitter.com/emilepetrone
.. _`Audrey Roy`: http://cartwheelweb.com/
.. _`Michael Delaney`: http://github.com/fusepilot/
.. _`John Campbell`: http://head3.com/
.. _`Phil Hughes`: http://www.linuxjournal.com/blogs/phil-hughes
