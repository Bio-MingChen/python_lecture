import click

@click.command()
@click.argument('name')  # 必填参数
@click.option('--age', default=18, help='你的年龄', type=int)  # 选项参数
@click.option('--city', type=click.Choice(['北京', '上海', '深圳'], case_sensitive=False), help='选择城市')  # 选项 + 选择限制
@click.option('--verbose', is_flag=True, help='是否开启详细模式')  # 旗标（布尔值）
def greet(name, age, city, verbose):
    """一个增强版的命令行问候程序"""
    msg = f"Hello, {name}! 你今年 {age} 岁"
    if city:
        msg += f"，来自 {city} 🌍"
    if verbose:
        msg += " （详细模式开启 ✅）"
    
    click.echo(msg)

if __name__ == '__main__':
    greet()

