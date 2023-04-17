import sys
import CloudFlare

def delete_all_dns_records(hostname, api_key, email):
    cf = CloudFlare.CloudFlare(email=email, token=api_key)

    try:
        zone_id = cf.zones.get(params={'name': hostname})[0]['id']
        records = cf.zones.dns_records.get(zone_id)

        for record in records:
            cf.zones.dns_records.delete(zone_id, record['id'])
            print(f"Deleted record {record['name']} ({record['type']})")

        print(f"All DNS records for {hostname} deleted.")
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print(f"Error deleting DNS records for {hostname}: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 delete_dns.py <hostname>")
        exit(1)

    hostname = sys.argv[1]
    api_key = "cbac2627c4d21e32be6cb73d1935aaceb1567"
    email = "limitedhighspeed@gmail.com"

    delete_all_dns_records(hostname, api_key, email)
