import click

def parse_fasta(fasta_file):
    """
    读入fasta文件并解析
    """
    fasta_dict = {}
    with open(fasta_file,"r",encoding="utf-8") as infile:
        seq = []
        gene = None
        for line in infile:
            line = line.strip() # 去掉结尾换行符
            if line.startswith(">"):
                if gene:
                    fasta_dict[gene] = "".join(seq)
                    gene = None
                    seq = []

                gene = line[1:]

            else:
                seq.append(line)

        # 保存最后一个基因的数据
        fasta_dict[gene] = "".join(seq)

    return fasta_dict

@click.command()
@click.argument("genename")
@click.option("--fasta_file","-f",help="fasta文件",default="./demo_seqs.fasta")
def main(genename,fasta_file):
    """
    根据基因名称查询fasta序列
    """
    fasta_dict = parse_fasta(fasta_file)

    if genename in fasta_dict:
        click.secho(f"查询到基因{genename}的序列如下：",fg="yellow")
        click.secho(f"{fasta_dict[genename]}",fg="green")
    else:
        click.secho(f"没有找到这个基因！",fg="red")

if __name__ == "__main__":
    main()