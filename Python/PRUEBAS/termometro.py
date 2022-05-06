def compute_closest_to_zero(ts):
    escala = sum(ts) / len(ts)
    if escala>=0:
        close_cero=min(ts)
    else:
        close_cero=max(ts)
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    return close_cero

medicion=[7,-10,13,8,-7,-1,6]
print(compute_closest_to_zero(medicion))