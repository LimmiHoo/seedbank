# === Stage 6: Поиск по нескольким словам ===
# Project: SeedBank
def parse_search_query(text):
    query = text.strip()
    if not query:
        return [], []
    terms = []
    exclusions = []
    for token in query.split():
        if token.startswith('-'):
            exclusions.append(token[1:].strip().lower())
        else:
            terms.append(token.lower())
    return terms, exclusions


def matches_all_terms(variant, terms):
    variant_text = ' '.join(
        [variant.get('name', '').lower()]
    )
    return all(term in variant_text for term in terms)


def matches_no_exclusions(variant, exclusions):
    variant_text = ' '.join(
        [variant.get('name', '').lower()]
    )
    return not any(exclusion in variant_text for exclusion in exclusions)


def filter_variants(variants, terms, exclusions):
    if not terms and not exclusions:
        return list(variants)
    result = []
    for variant in variants:
        if matches_all_terms(variant, terms) and matches_no_exclusions(variant, exclusions):
            result.append(variant)
    return result


if __name__ == '__main__':
    sample = [
        {'name': 'Розмарин', 'culture': 'трава'},
        {'name': 'Томат Черри', 'culture': 'овощ'},
        {'name': 'Пшеница', 'culture': 'зерно'},
        {'name': 'Мята', 'culture': 'трава'},
    ]
    found = filter_variants(sample, ['трав', '-мят'], [])
    for match in found:
        print(match['name'])
