package com.example.nerdherd;

import android.content.Context;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class EnterCodeActivity extends AppCompatActivity {

    Button enter_btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_enter_code);

        enter_btn = findViewById(R.id.enter_btn);

        enter_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Move to next page
                Context context = EnterCodeActivity.this;

            }
        });
    }
}
