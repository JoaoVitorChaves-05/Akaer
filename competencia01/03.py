import pandas as pd

def getTotalHours(group):
    group = group.sort_values(by="Start Time")[["Start Time", "End Time"]].values
    merged = []

    initial_start, initial_end = group[0]

    for start, end in group[1:]:
        if start <= initial_end:
            initial_end = max(initial_end, end)
        else:
            merged.append((initial_start, initial_end))
            initial_start, initial_end = start, end
    merged.append((initial_start, initial_end))
    total_hours = sum(pd.Timedelta(end - start).total_seconds() / 3600 for start, end in merged)
    return total_hours


df = pd.read_excel('DadosLicencas1.xlsx')

df["Start Time"] = pd.to_datetime(df["Start Time"], format="%d/%m/%Y %H:%M")
df["End Time"] = pd.to_datetime(df["End Time"], format="%Y-%m-%d %H:%M:%S")
df["Date"] = df["Start Time"].dt.date

resultados = []

for (day, user), grupo in df.groupby(["Date", "User Name"]):
    total = getTotalHours(grupo)
    resultados.append({
        "Day": day,
        "User Name": user,
        "Total Usage": total
    })

result_df = pd.DataFrame(resultados)
result_df["Total Usage"] = pd.to_timedelta(result_df["Total Usage"], unit='h')
result_df["Total Usage"] = result_df["Total Usage"].apply(lambda x: str(x).split(' ')[-1].split('.')[0])
result_df = result_df.sort_values(["Day", "User Name"], ascending=[True, True])
result_df.to_excel('ResultadoLicencas.xlsx', index=False)
print("ResultadoLicencas.xlsx criado com sucesso!")
print(result_df)