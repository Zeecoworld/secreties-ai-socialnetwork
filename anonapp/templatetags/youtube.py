from django import template
import re


register = template.Library()


def format_youtube(value):
    yt_link = re.compile(r'(https?://)?(www\.)?((youtu\.be/)|(youtube\.com/watch/?\?v=))([A-Za-z0-9-_]+)', re.I)
    yt_embed = '<iframe width="100%" height="100%" src="https://www.youtube.com/embed/{0}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    return yt_link.sub(lambda match: yt_embed.format(match.groups()[5]), value) 
    


register.filter('format_youtube',format_youtube)
