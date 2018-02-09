from django import template

from home.models import OurSkills

register = template.Library()
# Records snippet
@register.inclusion_tag('tags/skill.html', takes_context=True)
def get_all_skills(context):
    return {
        'our_skills': OurSkills.objects.all(),
        'request': context['request'],
    }