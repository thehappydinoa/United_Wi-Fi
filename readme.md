# United_Wi-Fi

Used to get flight info when connected to `United_Wi-Fi` network on United airplane.

## Resources

```bash
curl 'https://www.unitedwifi.com/portal/r/getAllSessionData' -H 'Pragma: no-cache' -H 'Accept: application/json, text/plain, */*' -H 'Referer: https://www.unitedwifi.com/portal/l/index' -H 'Cookie: UnitedAirlines=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX%XX'
```

## Notes

-   `01 Jan 0001 12:00 AM` means its does not know

## License

[License](LICENSE)
