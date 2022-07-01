def render_client(client) -> str:
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']))

    if client:
        template = env.get_template('client.html')
        s = template.render(title="Регистрация", client=client)
    else:
        template = env.get_template('message.html')
        s = template.render(title="Регистрация", message="Указан неверный ID")

    return s


def render_clients(clients) -> str:
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('clients.html')
    s = template.render(title="Регистрация", clients=clients)

    return s
