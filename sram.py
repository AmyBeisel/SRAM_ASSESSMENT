
import click
import requests

@click.command()

@click.option('--list', is_flag=True, help="will print everything")
@click.option('--bike_id',default=False, help="Enter the id of the bike you want to select")
@click.option('--fw_id', default=False, help="Enter the id of the front wheel you want to select")
@click.option('--rw_id', default=False, help="Enter the id of the rear wheel you want to select")


def main(list, bike_id, fw_id, rw_id):
    if list == True:
        bikes = requests.get("http://localhost:8000/Bike").json()
        click.echo('\nBikes')
        for b in bikes:
            click.echo(f"- Id: {b['id']}, Brand: {b['brand']}, Type: {b['bike_type']} , Weight: {b['weight']}")
        
        click.echo('\nFront Wheel')
        fw = requests.get("http://localhost:8000/FrontWheel/").json()
        for f in fw:
            click.echo(f"- Id: {f['id']}, Brand: {f['brand']}, Size: {f['size']}, Weight: {f['weight']}")
        
        click.echo('\nRear Wheel')
        rw = requests.get("http://localhost:8000/RearWheel/").json()
        for r in rw:
            click.echo(f"- Id: {r['id']}, Brand: {r['brand']}, Size: {r['size']}, Weight: {r['weight']}")
           

    if bike_id and fw_id and rw_id:
        click.echo('\n This shows the selected bike, front wheel, rear wheel and weight')
        abike = requests.get(f"http://localhost:8000/Bike/{bike_id}").json()
        click.echo(abike)
        afw = requests.get(f"http://localhost:8000/FrontWheel/{fw_id}").json()
        click.echo(afw)
        arw = requests.get(f"http://localhost:8000/RearWheel/{rw_id}").json()
        click.echo(arw)
        total_weight = abike['weight'] + afw['weight'] + arw['weight']
        #click.echo(total_weight)
        
        click.echo(f"\n You choose a great setup:\n - bike: {abike['brand']}, Front Wheel: {afw['brand']}, Rear Wheel: {arw['brand']}, total weight: {total_weight}")

if __name__ == "__main__":
    main()
