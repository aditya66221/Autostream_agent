def mock_lead_capture(name, email, platform):
    """
    Mock lead capture tool.

    In a production system, this could be replaced with
    a database, CRM API, or webhook integration.
    """

    print("\n✅ Lead captured successfully!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Platform: {platform}")