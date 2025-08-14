#!/usr/bin/env python3
"""
Database setup script for PHDA project.
Creates the body_composition table in Supabase.
"""

from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_body_composition_table():
    """Create the body_composition table with required schema."""
    
    # SQL to create the table
    sql = """
    CREATE TABLE IF NOT EXISTS body_composition (
        id SERIAL PRIMARY KEY,
        datetime TIMESTAMPTZ NOT NULL,
        weight DECIMAL(5,2) NOT NULL CHECK (weight > 0 AND weight < 1000),
        smm DECIMAL(5,2) NOT NULL CHECK (smm > 0 AND smm < 500),
        pbf DECIMAL(4,2) NOT NULL CHECK (pbf >= 0 AND pbf <= 100),
        ecw_tbw DECIMAL(4,3) NOT NULL CHECK (ecw_tbw >= 0 AND ecw_tbw <= 1),
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW()
    );
    
    -- Create an index on datetime for faster queries
    CREATE INDEX IF NOT EXISTS idx_body_composition_datetime 
    ON body_composition(datetime DESC);
    
    -- Create a trigger to update the updated_at column
    CREATE OR REPLACE FUNCTION update_updated_at_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = NOW();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    
    CREATE TRIGGER IF NOT EXISTS update_body_composition_updated_at 
        BEFORE UPDATE ON body_composition 
        FOR EACH ROW 
        EXECUTE FUNCTION update_updated_at_column();
    """
    
    try:
        # Initialize Supabase client
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key:
            raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables are required")
        
        supabase = create_client(supabase_url, supabase_key)
        
        # Execute the SQL
        result = supabase.rpc('exec_sql', {'sql': sql}).execute()
        
        print("✅ Database setup completed successfully!")
        print("   - body_composition table created")
        print("   - Validation constraints added")
        print("   - Indexes and triggers configured")
        
        return True
        
    except Exception as e:
        print(f"❌ Database setup failed: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Ensure your .env file contains valid SUPABASE_URL and SUPABASE_KEY")
        print("2. Verify your Supabase project has RPC functions enabled")
        print("3. Check that your API key has sufficient permissions")
        return False

if __name__ == "__main__":
    print("Setting up PHDA database...")
    success = create_body_composition_table()
    exit(0 if success else 1)