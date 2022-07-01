def render_message(msg):
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('message.html')
    s = template.render(title="Регистрация", message=msg)

    return s
