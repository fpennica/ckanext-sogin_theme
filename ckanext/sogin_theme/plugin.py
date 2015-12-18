import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Sogin_ThemePlugin(plugins.SingletonPlugin):
    '''
    SOGIN theme plugin
    '''
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'sogin_theme')
