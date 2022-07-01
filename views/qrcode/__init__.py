def render_qrcode(img_data):
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template('qrcode.html')
    s = template.render(title="Регистрация", img=img_data)

    return s
