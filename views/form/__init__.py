def render_form() -> str:
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('form.html')
    s = template.render(title="Регистрация")

    return s
