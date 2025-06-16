from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    if not request:
        return ''

    current_path = request.path

    menu_items = list(
        MenuItem.objects
        .filter(menu__name=menu_name)
        .select_related('parent')
        .order_by('order')
    )

    # Build relationship tree
    children_tree = {}
    id_to_item = {}
    for item in menu_items:
        children_tree.setdefault(item.parent_id, []).append(item)
        id_to_item[item.id] = item
        item.is_active = (item.get_url() == current_path)

    active_item = next((item for item in menu_items if item.is_active), None)

    # Identify visible items
    visible_ids = set()

    # Always show root items
    visible_ids.update(item.id for item in menu_items if item.parent_id is None)

    if active_item:
        # Show active item
        visible_ids.add(active_item.id)

        # Show all parents for active item
        parent = active_item.parent
        while parent:
            visible_ids.add(parent.id)
            parent = parent.parent

        # Show first level children...
        # 1. for active item
        visible_ids.update(child.id for child in children_tree.get(active_item.id, []))

        # 2. for all parents of active item
        parent = active_item.parent
        while parent:
            visible_ids.update(child.id for child in children_tree.get(parent.id, []))
            parent = parent.parent

    # Add children, add visible flag
    for item in menu_items:
        item.sub_items = [child for child in children_tree.get(item.id, []) if child.id in visible_ids]
        item.is_visible = item.id in visible_ids

    return {
        'menu_items': [item for item in menu_items if item.parent_id is None],
        'active_id': active_item.id if active_item else None,
    }
