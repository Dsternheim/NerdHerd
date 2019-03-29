package com.example.nerdherd;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;

public class ProfileActivity extends AppCompatActivity {
    Button save_changes;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        save_changes = findViewById(R.id.save_changes_btn);
    }
}
