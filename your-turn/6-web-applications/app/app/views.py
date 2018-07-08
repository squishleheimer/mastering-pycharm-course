from pyramid.view import view_config

from app.fake_data import get_orders

orders = get_orders()

@view_config(route_name='home', renderer="templates/mytemplate.pt")
def my_view(_):
    return {'project': 'app', 'orders': orders}
