"""

add a new item into the dict
usage example: python3 add.py 'istio' '/ɪztiːəʊ/' '' 'An open platform'

"""
import sys


def main():
    m = {}
    strl = []
    titleList = []
    count = 0
    if len(sys.argv) == 5:
        item = sys.argv[1]
        pron = sys.argv[2]
        note = sys.argv[3]
        desc = sys.argv[4]

        item = " {}  ".format(item)
        strl.append(item)
        m[item] = "|{}| {} | {} | {} |  ".format(item, pron, note, desc)
    with open("./README.md", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            count += 1

            # print(pattern.findall(line))
            l = line.split("|")
            if count <= 5:
                titleList.append(line)
            if count > 5:
                item = "|".join(l[1:2])
                strl.append(item)
                m[item] = line
    strl.sort()

    with open("./README.md", "w") as file:
        file.write("  \n".join(titleList) + "  \n")
        for i in strl:
            file.write(m[i] + "  \n")


if __name__ == '__main__':
    main()
    print("all done!please check ./README.md")

