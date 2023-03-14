import dill


def get_similarities() -> dict[int, dict[int, str]]:
    path = "similarities_pat_2.pkl"
    with open(path, "rb") as f:
        similarities_dict: dict[int, dict[int, str]] = dill.load(f)
    return similarities_dict


def add_0(similar) -> dict[int, dict[int, str]]:
    similar.update({0: {-4: "add_init_cons"}})
    return similar


def add_minus(similar):
    new_similar = {}
    for key in similar:
        value = similar[key]
        value.update({-1: "add_sound", -2: "no_sound", -3: "no_init_cons", -4: "add_init_cons"})
        new_similar[key] = value
    return new_similar


def write_similarities(similar) -> dict[int, dict[int, str]]:
    path = "similarities_pat.pkl"
    with open(path, "wb") as f:
        dill.dump(similar, f)
        print(f"{path} dumped")


if __name__ == "__main__":
    similarities = get_similarities()
    similarities = add_0(similarities)
    similarities = add_minus(similarities)
    similarities = dict(sorted(list(similarities.items())))
    write_similarities(similarities)
    print(similarities)
